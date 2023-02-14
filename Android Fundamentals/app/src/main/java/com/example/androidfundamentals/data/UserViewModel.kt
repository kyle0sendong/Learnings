package com.example.androidfundamentals.data

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

// Viewmodel : provide data to UI and survive configuration changes.
// acts as communication center between the repository and the UI
class UserViewModel(application: Application) : AndroidViewModel(application) {

    val readAllData: LiveData<List<User>>
    private val repository: UserRepository

    init {
        val userDao = UserDatabase.getDatabase(application).userDao()
        repository = UserRepository(userDao)
        readAllData = repository.readAllData
    }

    fun addUser(user: User) {
        //Viewmodel scope - part of co routines
        // Run this code in the background
        // Always launch database methods in background threads
        // Dont run in the main thread that is why viewModelScope is used
        viewModelScope.launch(Dispatchers.IO) {
            repository.addUser(user)
        }
    }
}