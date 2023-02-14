package com.example.androidfundamentals.data

import androidx.room.Entity
import androidx.room.PrimaryKey

// User table
// uses 'data class'
// data class user ( fields )

@Entity(tableName = "user_table") // Entity - table name
data class User(
    @PrimaryKey(autoGenerate = true) val id: Int, //id is the primary key using autogenerate
    val firstName: String,
    val lastName: String,
    val age: String
)