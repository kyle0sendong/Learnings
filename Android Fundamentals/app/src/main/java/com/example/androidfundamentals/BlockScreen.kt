package com.example.androidfundamentals

import android.graphics.Color
import android.graphics.PixelFormat
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.view.WindowManager
import android.widget.ImageView
import androidx.annotation.ContentView
import com.example.androidfundamentals.databinding.ActivityBlockScreenBinding
import kotlinx.android.synthetic.main.activity_block_screen.view.*

class BlockScreen : AppCompatActivity() {

    private lateinit var binding: ActivityBlockScreenBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        supportActionBar?.hide()
        super.onCreate(savedInstanceState)
        binding = ActivityBlockScreenBinding.inflate(layoutInflater)

        setContentView(binding.root, WindowManager.LayoutParams().apply {

            flags = WindowManager.LayoutParams.FLAG_LAYOUT_IN_SCREEN or
                    WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL or
                    WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE or
                    WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
            PixelFormat.TRANSLUCENT
            type = WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY

        })

    }

    override fun onBackPressed() {
        // Leave empty to disable
    }
}