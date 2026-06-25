package com.pranshul.whisperdeck

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    private lateinit var deckAdapter: DeckAdapter
    private lateinit var status: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        status = findViewById(R.id.status)
        deckAdapter = DeckAdapter { item ->
            status.text = getString(R.string.selected, item.name)
        }
        findViewById<RecyclerView>(R.id.deck_list).apply {
            layoutManager = LinearLayoutManager(this@MainActivity)
            adapter = deckAdapter
        }

        findViewById<Button>(R.id.record_btn).setOnClickListener { toggleRecording() }
        deckAdapter.submit(loadDeck())
    }

    private fun toggleRecording() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO)
            != PackageManager.PERMISSION_GRANTED
        ) {
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.RECORD_AUDIO), 41)
            return
        }
        ContextCompat.startForegroundService(this, Intent(this, RecorderService::class.java))
        status.text = getString(R.string.recording)
    }

    private fun loadDeck(): List<DeckItem> =
        listOf(DeckItem("meeting-notes", 12), DeckItem("podcast-draft", 3))
}
