package com.example.androidfundamentals

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent


class SampleBroadCastReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context?, intent: Intent?) {
        if(intent?.action == Intent.ACTION_USER_BACKGROUND ) {

        }
    }
}