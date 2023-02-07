package com.example.androidfundamentals

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.androidfundamentals.databinding.ActivitySampleRecyclerviewBinding

class SampleRecyclerview : AppCompatActivity() {

    private lateinit var binding: ActivitySampleRecyclerviewBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySampleRecyclerviewBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val todoList = mutableListOf(
            Todo("Follow Android", false),
            Todo("Take a rest", false)
        )

        val adapter = TodoAdapter(todoList)
        binding.sampleRvTodo.adapter = adapter
        binding.sampleRvTodo.layoutManager = LinearLayoutManager(this)
        binding.sampleAddTodo.setOnClickListener {
            val title = binding.sampleEtTodo.text.toString()
            val todo = Todo(title, false)
            todoList.add(todo)
            adapter.notifyItemInserted(todoList.size-1)
        }
    }
}