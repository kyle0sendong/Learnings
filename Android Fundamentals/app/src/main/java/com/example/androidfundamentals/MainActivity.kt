package com.example.androidfundamentals

import android.accessibilityservice.AccessibilityServiceInfo
import android.app.usage.UsageStatsManager
import android.content.*
import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.Settings
import android.util.Log
import android.view.accessibility.AccessibilityManager
import com.example.androidfundamentals.databinding.ActivityMainBinding
import com.example.androidfundamentals.samplePackageManager.SamplePackageManager
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        supportActionBar?.hide()
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val intentFilter = IntentFilter(Intent.ACTION_USER_BACKGROUND)
        val receiver = SampleBroadCastReceiver()
        registerReceiver(receiver, intentFilter)

        // Sample finding error/debug in LogCat Log.d = log debug, log.e -> log error etc.
        Log.d("Sample", "Hallo")
        checkAccessibilityPermission()


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

        binding.sampleRecyclerview.setOnClickListener {
            Intent(this, SampleRecyclerview::class.java).also {
                startActivity(it)
            }
        }

        binding.sampleFragments.setOnClickListener {
            Intent(this, SampleFragments::class.java).also {
                startActivity(it)
            }
        }

        binding.sampleBottomNav.setOnClickListener {
            Intent(this, SampleBottomNav::class.java).also {
                startActivity(it)
            }
        }

        binding.sampleRoom.setOnClickListener {
            Intent(this, SampleRoom::class.java).also {
                startActivity(it)
            }
        }

        binding.capturePhoto.setOnClickListener{
            Intent(this, CapturePhoto::class.java).also {
                startActivity(it)
            }
        }

        binding.samplePackageManager.setOnClickListener{
            Intent(this, SamplePackageManager::class.java).also {
                startActivity(it)
            }
        }

    }

    private fun checkAccessibilityPermission() {
        val accessibilityManager = getSystemService(Context.ACCESSIBILITY_SERVICE) as AccessibilityManager
        val isAccessibilityEnabled = accessibilityManager.isEnabled

        if (!isAccessibilityEnabled) {
            Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS).also {
                startActivity(it)
            }
        }
    }

//    override fun onStop() {
//        super.onStop()
//        val usageStatsManager = getSystemService(Context.USAGE_STATS_SERVICE) as UsageStatsManager
//
//        val currentTime = System.currentTimeMillis()
//
//        val stats = usageStatsManager.queryUsageStats(UsageStatsManager.INTERVAL_BEST, currentTime - 1000 * 10, currentTime)
//
//        if (stats != null) {
//            stats.sortedByDescending { it.lastTimeUsed }.firstOrNull()?.let {
//                val packageName = it.packageName
//                val appName = packageManager.getApplicationLabel(packageManager.getApplicationInfo(packageName, PackageManager.GET_META_DATA)).toString()
//                binding.testview.text = "User opened app: $appName ($packageName)"
//                Log.d(ContentValues.TAG, "User opened app: $appName ($packageName)")
//            }
//        }
//    }

    //Overriding life cycle of activity
    // onCreate() -> onStart() -> onResume()
    // onPause() -> onStop()
    // onDestroy() -> onRestart()

    //sample implementation of overriding lifecycle
    override fun onDestroy() {
        super.onDestroy()
    }


}