package com.example.androidfundamentals.fragments.update

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.example.androidfundamentals.R
import com.example.androidfundamentals.databinding.FragmentUpdateBinding
import com.example.androidfundamentals.model.User
import com.example.androidfundamentals.viewmodel.UserViewModel
import kotlinx.android.synthetic.main.fragment_update.*

class UpdateFragment : Fragment() {

    private var _binding: FragmentUpdateBinding? = null
    private val binding get() = _binding!!

    private val args by navArgs<UpdateFragmentArgs>()

    private lateinit var mUserViewModel: UserViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentUpdateBinding.inflate(inflater, container, false)
        mUserViewModel = ViewModelProvider(this)[UserViewModel::class.java]

        // Safeargs for filling up the edit text with current user's info
        binding.roomUpdateFname.setText(args.currentUser.firstName)
        binding.roomUpdateLname.setText(args.currentUser.lastName)
        binding.roomUpdateAge.setText(args.currentUser.age)

        binding.roomUpdateBtn.setOnClickListener{
            updateItem()
        }

        return binding.root
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun updateItem(){
        val firstName = binding.roomUpdateAge.text.toString()
        val lastName = binding.roomUpdateLname.text.toString()
        val age = binding.roomUpdateAge.text.toString()

        if(checkInput(firstName, lastName, age)) {
            val updatedUser = User(args.currentUser.id, firstName, lastName, age)
            mUserViewModel.updateUser(updatedUser)
            Toast.makeText(requireContext(), "Updated $firstName $lastName", Toast.LENGTH_SHORT).show()
            findNavController().navigate(R.id.action_updateFragment_to_listFragment)
        }
    }

    private fun checkInput(fname: String, lname: String, age: String): Boolean {
        return !(fname.isEmpty() && lname.isEmpty() && age.isEmpty())
    }
}
