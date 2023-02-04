package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    //Overriding life cycle of activity
    // onCreate() -> onStart() -> onResume()
    // onPause() -> onStop()
    // onDestroy() -> onRestart()

    //sample implementation of overriding lifecycle
    override fun onDestroy() {
        super.onDestroy()
    }


}