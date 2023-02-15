package com.example.androidfundamentals.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import com.example.androidfundamentals.model.User

/*
    Database contains database holder and serves as the main access point for
    connection to your app's relational data
*/

@Database(entities = [User::class], version = 1, exportSchema = false)  //exportSchema false for version control
abstract class UserDatabase: RoomDatabase() {   // Inherits from RoomDatebase()

    abstract fun userDao(): UserDao // returns a UserDao

    companion object {
        @Volatile
        private var INSTANCE: UserDatabase? = null  // only 1 instance of a class

        // Check if instance of database exists
        fun getDatabase(context: Context): UserDatabase {
            val tempInstance = INSTANCE

            if(tempInstance != null) {
                return tempInstance
            }

            synchronized(this) { //create new instance using synchronized if instance is null
                val instance = Room.databaseBuilder(    //build a database
                    context.applicationContext,
                    UserDatabase::class.java,
                    "user_database"
                ).build()
                INSTANCE = instance
                return instance
            }
        }
    }

}