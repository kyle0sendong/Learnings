package com.example.androidfundamentals.fragments.add

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import com.example.androidfundamentals.R
import com.example.androidfundamentals.model.User
import com.example.androidfundamentals.viewmodel.UserViewModel
import com.example.androidfundamentals.databinding.FragmentAddBinding

class AddFragment : Fragment() {

    private lateinit var binding: FragmentAddBinding
    private lateinit var mUserViewModel: UserViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        binding = FragmentAddBinding.inflate(inflater, container, false)
        mUserViewModel = ViewModelProvider(this)[UserViewModel::class.java]

        binding.roomAddBtn.setOnClickListener {
            insertToDatabase()
        }
        return binding.root
    }

    private fun insertToDatabase() {
        val fname = binding.roomFname.text.toString()
        val lname = binding.roomLname.text.toString()
        val age = binding.roomAge.text.toString()

        if (checkInput(fname, lname, age)) {
            val user = User(0, fname, lname, age) // create User object
            mUserViewModel.addUser(user)
            Toast.makeText(requireContext(), "$fname $lname added successfully", Toast.LENGTH_SHORT).show() // prompt toast
            findNavController().navigate(R.id.action_addFragment_to_listFragment) // navigate back to list fragment
        } else {
            Toast.makeText(requireContext(), "Fill all fields", Toast.LENGTH_SHORT).show()
        }

    }

    private fun checkInput(fname: String, lname: String, age: String): Boolean {
        return !(fname.isEmpty() && lname.isEmpty() && age.isEmpty())
    }

}