package com.example.androidfundamentals.repository

import androidx.lifecycle.LiveData
import com.example.androidfundamentals.data.UserDao
import com.example.androidfundamentals.model.User

// Repository : class that abstracts access to multiple data sources.
class UserRepository (private val userDao: UserDao) {

    val readAllData: LiveData<List<User>> = userDao.readAllData()

    suspend fun addUser(user: User) {
        userDao.addUser(user)
    }

}