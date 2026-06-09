import React from 'react';
import { FileText, Activity, Clock } from 'lucide-react';

export const WorkerPanels = ({ project }) => {
  return (
    <div className="w-80 flex flex-col bg-card">
      <div className="p-4 border-b flex items-center gap-2">
        <Activity size={18} className="text-primary" />
        <h3 className="font-bold">Agent Activity</h3>
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-6">
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium">Competitor Agent</span>
            <span className="text-[10px] px-2 py-0.5 rounded-full bg-green-500/10 text-green-500">Idle</span>
          </div>
          <div className="p-3 border rounded-lg space-y-2 bg-muted/20">
            <div className="flex items-center gap-2 text-xs text-muted-foreground">
              <Clock size={12} />
              Last run: Never
            </div>
            <button className="flex items-center gap-2 text-xs text-primary font-medium hover:underline">
              <FileText size={12} />
              View Last Report
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
