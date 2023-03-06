package com.example.androidfundamentals.samplePackageManager

import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.annotation.RequiresApi
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.androidfundamentals.R
import com.example.androidfundamentals.databinding.ActivitySamplePackageManagerBinding
import kotlinx.android.synthetic.main.activity_sample_package_manager.*

class SamplePackageManager : AppCompatActivity() {

    private lateinit var binding: ActivitySamplePackageManagerBinding

    @RequiresApi(Build.VERSION_CODES.M)
    override fun onCreate(savedInstanceState: Bundle?) {
        binding = ActivitySamplePackageManagerBinding.inflate(layoutInflater)
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        // Create an Intent to match all main launcher activities
        val intent = Intent(Intent.ACTION_MAIN)
        intent.addCategory(Intent.CATEGORY_LAUNCHER)

        // Get the PackageManager instance
        val packageManager = this.packageManager

        // Query the list of all installed applications that can handle the intent
        val resolveInfoList = packageManager?.queryIntentActivities(intent, PackageManager.MATCH_ALL)

        val testList = mutableListOf<AppInfo>()

        // Loop through the list of resolved activities and their application info
        if (resolveInfoList != null) {
            for (resolveInfo in resolveInfoList) {
                val packageName = resolveInfo.activityInfo.packageName
                val applicationInfo = packageManager.getApplicationLabel(resolveInfo.activityInfo.applicationInfo).toString()

                val appInfo = AppInfo(packageName, applicationInfo)
                testList.add(appInfo)
            }
        }

        val adapter = AppInfoAdapter(testList)
        binding.rvAllApplication.adapter = adapter
        binding.rvAllApplication.layoutManager = LinearLayoutManager(this)
    }
}