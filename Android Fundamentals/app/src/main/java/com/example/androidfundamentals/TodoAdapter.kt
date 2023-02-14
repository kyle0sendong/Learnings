package com.example.androidfundamentals

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.androidfundamentals.databinding.SampleItemTodoBinding


class TodoAdapter(var todos: List<Todo>): RecyclerView.Adapter<TodoAdapter.ToDoViewHolder>() {

    //Before:
    //inner class ToDoViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView)
    inner class ToDoViewHolder(val binding: SampleItemTodoBinding) : RecyclerView.ViewHolder(binding.root)


    //Before : error prone
    //    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ToDoViewHolder {
    //        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_todo, parent, false)
    //        return ToDoViewHolder(view)
    //    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ToDoViewHolder {
        val layoutInflater = LayoutInflater.from(parent.context)
        val binding = SampleItemTodoBinding.inflate(layoutInflater, parent, false)
        return ToDoViewHolder(binding)
    }


    override fun onBindViewHolder(holder: ToDoViewHolder, position: Int) {
        holder.binding.apply {
            tvTitle.text = todos[position].title
            cbDone.isChecked = todos[position].isChecked
        }
    }

    override fun getItemCount(): Int {
        return  todos.size
    }

}