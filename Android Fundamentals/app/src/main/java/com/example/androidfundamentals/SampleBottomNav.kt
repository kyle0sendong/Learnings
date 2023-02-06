package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.androidfundamentals.databinding.ActivitySampleBottomNavBinding

class SampleBottomNav : AppCompatActivity() {

    private lateinit var binding: ActivitySampleBottomNavBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleBottomNavBinding.inflate(layoutInflater)
        setContentView(binding.root)

    }
}