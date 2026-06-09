'use client';

import React, { useState } from 'react';
import { Layout, Sidebar, PlannerChat, WorkerPanels } from '../components/workspace';

export default function Home() {
  const [activeProject, setActiveProject] = useState(null);

  if (!activeProject) {
    return <Onboarding onProjectCreate={setActiveProject} />;
  }

  return (
    <div className="flex h-screen bg-background">
      <Sidebar project={activeProject} />
      <main className="flex-1 flex flex-col overflow-hidden">
        <div className="flex-1 flex overflow-hidden">
          <PlannerChat project={activeProject} />
          <WorkerPanels project={activeProject} />
        </div>
      </main>
    </div>
  );
}

function Onboarding({ onProjectCreate }) {
  return (
    <div className="flex flex-col items-center justify-center h-screen space-y-8">
      <h1 className="text-4xl font-bold">StartupOS</h1>
      <button
        onClick={() => onProjectCreate({ name: "Demo Project" })}
        className="px-6 py-3 bg-primary text-white rounded-lg"
      >
        Create New Project
      </button>
    </div>
  );
}
