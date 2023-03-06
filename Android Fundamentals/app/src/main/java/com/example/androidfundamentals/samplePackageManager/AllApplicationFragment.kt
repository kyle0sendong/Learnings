package com.example.androidfundamentals.samplePackageManager

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.androidfundamentals.R
import com.example.androidfundamentals.databinding.FragmentAllApplicationBinding
import android.content.pm.PackageManager

class AllApplicationFragment : Fragment() {

    private var _binding: FragmentAllApplicationBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        _binding = FragmentAllApplicationBinding.inflate(inflater, container, false)


        // Create an Intent to match all main launcher activities
        val intent = Intent(Intent.ACTION_MAIN)
        intent.addCategory(Intent.CATEGORY_LAUNCHER)

        // Get the PackageManager instance
        val packageManager = context?.packageManager

        // Query the list of all installed applications that can handle the intent
        val resolveInfoList = packageManager?.queryIntentActivities(intent, PackageManager.MATCH_ALL)

        val testList = mutableListOf<AppInfo>()

        // Loop through the list of resolved activities and their application info
        if (resolveInfoList != null) {
            for (resolveInfo in resolveInfoList) {
                val packageName = resolveInfo.activityInfo.packageName
                val applicationInfo = packageManager.getApplicationInfo(packageName, PackageManager.GET_META_DATA).toString()

                val appInfo = AppInfo(packageName, applicationInfo)
                testList.add(appInfo)
            }
        }



        // Get all application names store it in adapter
        // val allApps = etc.
        // val adapter = AppInfoAdapter

        return binding.root
    }

    fun getInstalledAppsNames(packageManager: PackageManager): List<String> {
        val apps = packageManager.getInstalledApplications(PackageManager.GET_META_DATA)
        val appNames = mutableListOf<String>()
        for (app in apps) {
            appNames.add(packageManager.getApplicationLabel(app).toString())
        }
        return appNames
    }
    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }


}