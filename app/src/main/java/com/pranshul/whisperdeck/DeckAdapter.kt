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
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val v = LayoutInflater.from(parent.context)
            .inflate(android.R.layout.simple_list_item_1, parent, false)
        return Holder(v)
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val item = items[position]
        holder.title.text = "${item.name} - ${item.ageDays}d"
        holder.itemView.setOnClickListener { onClick(item) }
    }
