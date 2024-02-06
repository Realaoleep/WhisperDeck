package com.pranshul.whisperdeck

import android.app.Notification
import android.app.Service
import android.content.Intent
import android.media.MediaRecorder
import android.os.IBinder
import java.io.File

class RecorderService : Service() {

    private var recorder: MediaRecorder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        startForeground(11, buildNotification())
        startRecording()
        return START_STICKY
    }

    private fun startRecording() {
        val out = File(getExternalFilesDir(null), "deck-${System.currentTimeMillis()}.m4a")
        recorder = (recorder ?: MediaRecorder()).apply {