package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.androidfundamentals.databinding.ActivitySampleFragmentsBinding

class SampleFragments : AppCompatActivity() {

    private lateinit var binding: ActivitySampleFragmentsBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleFragmentsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val firstFragment = FirstFragment()

        binding.fragmentButton1.setOnClickListener {
            supportFragmentManager.beginTransaction().apply {
                replace(R.id.sample_fragment_framelayout, firstFragment)
                addToBackStack(null)
                commit()
            }
        }

        val secondFragment = SecondFragment()
        binding.fragmentButton2.setOnClickListener {
            supportFragmentManager.beginTransaction().apply {
                replace(R.id.sample_fragment_framelayout, secondFragment)
                addToBackStack(null)
                commit()
            }
        }
    }
}