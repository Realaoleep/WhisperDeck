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
            setAudioSource(MediaRecorder.AudioSource.MIC)
            setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            setAudioEncoder(MediaRecorder.AudioEncoder.AAC)
            setOutputFile(out.absolutePath)
            prepare()
            start()
        }
    }

    private fun buildNotification(): Notification = Notification.Builder(this, "deck")
        .setContentTitle(getString(R.string.app_name))
        .setContentText(getString(R.string.recording))
        .setSmallIcon(android.R.drawable.ic_btn_speak_now)
        .build()

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onDestroy() {
        recorder?.apply { stop(); release() }
        recorder = null
        super.onDestroy()
    }
}
