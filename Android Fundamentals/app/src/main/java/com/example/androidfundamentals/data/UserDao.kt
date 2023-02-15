package com.example.androidfundamentals.data

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.example.androidfundamentals.model.User

// DAO - Data Access Object - contains methods used for accessing a database
// @ is annotate
@Dao
interface UserDao {

    // Inserting data
    // If there is exactly the same user, just ignore. (ignore duplicates using onConflict)
    // 'Suspend' will be used for the co routines
    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun addUser(user: User)

    // SQL command for reading
    @Query("SELECT * FROM user_table ORDER BY id ASC")
    fun readAllData(): LiveData<List<User>>

}