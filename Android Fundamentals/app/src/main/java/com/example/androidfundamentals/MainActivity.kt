package com.example.androidfundamentals

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import com.example.androidfundamentals.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Sample finding error/debug in LogCat Log.d = log debug, log.e -> log error etc.
        Log.d("Sample", "Hallo")

        binding.sampleLayout.setOnClickListener {
            Intent(this, SampleLayout::class.java).also {
                startActivity(it)
            }
        }

        binding.sampleEditText.setOnClickListener {
            Intent(this, SampleEditText::class.java).also {
                startActivity(it)
            }
        }

        binding.sampleBottomNav.setOnClickListener {
            Intent(this, SampleBottomNav::class.java).also {
                startActivity(it)
            }
        }
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