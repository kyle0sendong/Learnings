package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.androidfundamentals.databinding.ActivitySampleEditTextBinding

class SampleEditText : AppCompatActivity() {
    private lateinit var binding: ActivitySampleEditTextBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleEditTextBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.sampleEditTextButton1.setOnClickListener {
            val firstNumber = binding.editTextNumber1.text.toString().toInt()
            val secondNumber = binding.editTextNumber2.text.toString().toInt()
            val result = firstNumber + secondNumber
            binding.sampleEditTextView1.text = result.toString()
        }
    }
}