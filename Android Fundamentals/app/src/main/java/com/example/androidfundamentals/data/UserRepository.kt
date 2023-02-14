package com.example.androidfundamentals.data

import androidx.lifecycle.LiveData

// Repository : class that abstracts access to multiple data sources.
class UserRepository (private val userDao: UserDao) {

    val readAllData: LiveData<List<User>> = userDao.readAllData()

    suspend fun addUser(user: User) {
        userDao.addUser(user)
    }

}