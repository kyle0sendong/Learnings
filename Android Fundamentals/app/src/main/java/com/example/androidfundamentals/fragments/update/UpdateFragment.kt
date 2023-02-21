package com.example.androidfundamentals.fragments.update

import android.app.AlertDialog
import android.os.Bundle
import android.view.*
import androidx.fragment.app.Fragment
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.core.view.MenuHost
import androidx.core.view.MenuProvider
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.example.androidfundamentals.R
import com.example.androidfundamentals.databinding.FragmentUpdateBinding
import com.example.androidfundamentals.model.User
import com.example.androidfundamentals.viewmodel.UserViewModel


class UpdateFragment : Fragment(), MenuProvider {

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

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        activity?.addMenuProvider(this, viewLifecycleOwner, Lifecycle.State.RESUMED)
    }

    override fun onCreateMenu(menu: Menu, menuInflater: MenuInflater) {
        menuInflater.inflate(R.menu.delete_menu, menu)
    }

    override fun onMenuItemSelected(menuItem: MenuItem): Boolean {
        if(menuItem.itemId ==  R.id.delete_menu) {
            deleteUser()
            return true
        }
        return false
    }

    private fun deleteUser() {
        val builder = AlertDialog.Builder(requireContext())
        builder.setPositiveButton("Yes") { _, _ ->
            mUserViewModel.deleteUser(args.currentUser)
            Toast.makeText(
                requireContext(),
                "Successfully removed: ${args.currentUser.firstName}",
                Toast.LENGTH_SHORT).show()
            findNavController().navigate(R.id.action_updateFragment_to_listFragment)
        }
        builder.setNegativeButton("No") { _, _ -> }
        builder.setTitle("Delete ${args.currentUser.firstName}?")
        builder.setMessage("Are you sure you want to delete ${args.currentUser.firstName}?")
        builder.create().show()
    }

    private fun updateItem(){
        val firstName = binding.roomUpdateFname.text.toString()
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

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

}
