import React, { useState } from 'react';
import { Send } from 'lucide-react';

export const PlannerChat = ({ project }) => {
  const [messages, setMessages] = useState([
    { role: 'agent', content: 'Hello! I am your Planner Agent. I have analyzed your Startup Vision. What would you like to focus on first?' }
  ]);

  return (
    <div className="flex-1 flex flex-col border-r bg-muted/30">
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[80%] p-3 rounded-2xl ${m.role === 'user' ? 'bg-primary text-white' : 'bg-card border shadow-sm'}`}>
              {m.content}
            </div>
          </div>
        ))}
      </div>
      <div className="p-4 bg-background border-t">
        <div className="flex gap-2 p-2 border rounded-xl focus-within:ring-2 ring-primary/20 bg-card">
          <input
            className="flex-1 bg-transparent border-none focus:outline-none px-2 text-sm"
            placeholder="Talk to Planner..."
          />
          <button className="p-2 bg-primary text-white rounded-lg">
            <Send size={18} />
          </button>
        </div>
      </div>
    </div>
  );
};
