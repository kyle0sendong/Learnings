package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.androidfundamentals.databinding.ActivitySampleLayoutBinding

class SampleLayout : AppCompatActivity() {

    private lateinit var binding: ActivitySampleLayoutBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleLayoutBinding.inflate(layoutInflater)
        setContentView(binding.root)

    }
}