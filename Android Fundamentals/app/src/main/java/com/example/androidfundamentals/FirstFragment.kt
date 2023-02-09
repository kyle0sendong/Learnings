package com.example.androidfundamentals

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.fragment.app.Fragment


class FirstFragment : Fragment() {


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_first, container, false)

        val fr1_text = view.findViewById<TextView>(R.id.fr1_text)
        val fr1_btn1 = view.findViewById<Button>(R.id.fr1_btn1)

        fr1_btn1.setOnClickListener {
            fr1_text.text = "Button clicked nice"
        }

        return view
    }



}