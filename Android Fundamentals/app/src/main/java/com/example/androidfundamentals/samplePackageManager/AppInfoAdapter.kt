package com.example.androidfundamentals.samplePackageManager

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.androidfundamentals.databinding.ItemApplicationBinding

class AppInfoAdapter(var apps: List<AppInfo>): RecyclerView.Adapter<AppInfoAdapter.AppInfoViewHolder>() {

    inner class AppInfoViewHolder(val binding: ItemApplicationBinding): RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): AppInfoViewHolder {
        val layoutInflater = LayoutInflater.from(parent.context)
        val binding = ItemApplicationBinding.inflate(layoutInflater, parent, false)
        return AppInfoViewHolder(binding)
    }

    override fun onBindViewHolder(holder: AppInfoViewHolder, position: Int) {
        holder.binding.apply {
            tvApplicationName.text = apps[position].appName
            tvApplicationPackageName.text = apps[position].appPackageName
        }
    }

    override fun getItemCount(): Int {
        return apps.size
    }

}