package com.example.androidfundamentals.fragments.list

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.androidfundamentals.data.User
import com.example.androidfundamentals.databinding.CustomRowBinding


class ListAdapter(): RecyclerView.Adapter<ListAdapter.MyViewHolder>() {

    inner class MyViewHolder(val binding: CustomRowBinding) : RecyclerView.ViewHolder(binding.root)
    private var userList = emptyList<User>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val layoutInflater = LayoutInflater.from(parent.context)
        val binding = CustomRowBinding.inflate(layoutInflater, parent, false)
        return MyViewHolder(binding)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        var currentItem = userList[position]
        holder.binding.apply {
            userFname.text = currentItem.firstName
            userLname.text = currentItem.lastName
            userAge.text = currentItem.age
        }
    }

    override fun getItemCount(): Int {
        return userList.size
    }

    fun setData(user: List<User>) {
        this.userList = user
        notifyDataSetChanged()
    }

}