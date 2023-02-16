package com.example.androidfundamentals.model

import android.os.Parcelable
import androidx.room.Entity
import androidx.room.PrimaryKey
import kotlinx.android.parcel.Parcelize

// User table
// uses 'data class'
// data class user ( fields )
@Parcelize // Annotate percalable
@Entity(tableName = "user_table") // Entity - table name
data class User(
    @PrimaryKey(autoGenerate = true) val id: Int, //id is the primary key using autogenerate
    val firstName: String,
    val lastName: String,
    val age: String
) : Parcelable // To be able to pass user object