package com.example.androidfundamentals

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.androidfundamentals.databinding.ActivitySampleLayoutBinding

class SampleLayout : AppCompatActivity() {

    private lateinit var binding: ActivitySampleLayoutBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleLayoutBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.applyButton.setOnClickListener {
            val firstName = binding.firstName.text.toString()
            val lastName = binding.lastName.text.toString()
            val country = binding.countryOrigin.text.toString()
            // Can use Class Serializable
            Intent(this, SampleExtraIntent::class.java).also {
                it.putExtra("EXTRA_FNAME", firstName)
                it.putExtra("EXTRA_LNAME", lastName)
                it.putExtra("EXTRA_COUNTRY", country)
                startActivity(it)
            }
        }
    }
}