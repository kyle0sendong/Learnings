package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.example.androidfundamentals.databinding.ActivitySampleBottomNavBinding

class SampleBottomNav : AppCompatActivity() {

    private lateinit var binding: ActivitySampleBottomNavBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleBottomNavBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val homeFragment = FirstFragment()
        val userFragment = SecondFragment()

        setFragment(homeFragment)

        binding.btmNav.setOnItemSelectedListener {

            when(it.itemId) {
                R.id.nav_home -> {setFragment(homeFragment)}

                R.id.nav_user -> {setFragment(userFragment)}

                else -> { true }
            }

        }

    }

    private fun setFragment(fragment: Fragment): Boolean{
        supportFragmentManager.beginTransaction().apply {
            replace(R.id.nav_btm, fragment)
            addToBackStack(null)
            commit()
        }
        return true
    }
}