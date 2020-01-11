import React, { useState } from 'react';
import Events, { EVENTS_ROUTE } from "./Events";
import Places, { PLACES_ROUTE } from "./Places";
import './App.css';
import './bootstrap.min.css';

function Router({ route }) {
  switch (route) {
    case EVENTS_ROUTE:
      return <Events/>;
    case PLACES_ROUTE:
      return <Places/>;
    default:
      return <p>Route not found</p>
  }
}

function App() {
  const [route, setRoute] = useState(EVENTS_ROUTE);
  return (
    <div className="App">
      <ul>
        <li><a onClick={() => setRoute(EVENTS_ROUTE)}>Events</a></li>
        <li><a onClick={() => setRoute(PLACES_ROUTE)}>Places</a></li>
      </ul>
      <div>
        <Router route={route}/>
      </div>
    </div>
  );
}

export default App;
