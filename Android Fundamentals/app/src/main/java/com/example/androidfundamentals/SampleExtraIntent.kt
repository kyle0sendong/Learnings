package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.androidfundamentals.databinding.ActivitySampleExtraIntentBinding

class SampleExtraIntent : AppCompatActivity() {

    private lateinit var binding: ActivitySampleExtraIntentBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleExtraIntentBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val name = intent.getStringExtra("EXTRA_FNAME") + " " + intent.getStringExtra("EXTRA_LNAME")
        val country = intent.getStringExtra("EXTRA_COUNTRY")
        val stringText = "Hi, $name from $country"

        binding.extraIntentTextView1.text = stringText


    }
}