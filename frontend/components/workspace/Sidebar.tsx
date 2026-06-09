import React from 'react';
import { User, Settings, Folder, ShieldCheck } from 'lucide-react';

export const Sidebar = ({ project }) => {
  return (
    <aside className="w-64 bg-card border-r flex flex-col">
      <div className="p-6 border-b">
        <h2 className="text-xl font-bold truncate">{project.name}</h2>
      </div>
      <nav className="flex-1 p-4 space-y-2">
        <div className="flex items-center gap-3 p-2 rounded-lg bg-primary/10 text-primary">
          <ShieldCheck size={20} />
          <span className="font-medium">Planner Agent</span>
        </div>
        <div className="pt-4 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
          Worker Agents
        </div>
        {/* Map through worker agents here */}
        <div className="text-sm p-2 text-muted-foreground italic">
          No workers selected
        </div>
      </nav>
      <div className="p-4 border-t space-y-2">
        <button className="flex items-center gap-3 w-full p-2 hover:bg-muted rounded-lg text-sm">
          <Folder size={18} />
          Workspace Folder
        </button>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-muted rounded-lg text-sm">
          <Settings size={18} />
          NVIDIA API Settings
        </button>
      </div>
    </aside>
  );
};
