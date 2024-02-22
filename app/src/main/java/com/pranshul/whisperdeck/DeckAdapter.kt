package com.pranshul.whisperdeck

import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

data class DeckItem(val name: String, val ageDays: Int)

class DeckAdapter(private val onClick: (DeckItem) -> Unit) :
    RecyclerView.Adapter<DeckAdapter.Holder>() {

    private val items = mutableListOf<DeckItem>()

    fun submit(next: List<DeckItem>) {
        items.clear(); items.addAll(next); notifyDataSetChanged()
    }

    class Holder(v: android.view.View) : RecyclerView.ViewHolder(v) {
        val title: TextView = v.findViewById(android.R.id.text1)