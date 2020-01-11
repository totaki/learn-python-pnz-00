import React, { useState } from 'react';
import Events, { EVENTS_ROUTE } from "./Events";
import Places, { PLACES_ROUTE } from "./Places";
import './App.css';
import './bootstrap.min.css';

function Router({ route, setRoute }) {
  switch (route) {
    case EVENTS_ROUTE:
      return <Events setRoute={setRoute}/>;
    case PLACES_ROUTE:
      return <Places/>;
    default:
      return <p>Route not found</p>
  }
}

function App() {
  const [route, setRoute] = useState(EVENTS_ROUTE);
  return (
    <div className="container">
      <ul>
        <li><a onClick={() => setRoute(EVENTS_ROUTE)}>Events</a></li>
        <li><a onClick={() => setRoute(PLACES_ROUTE)}>Places</a></li>
      </ul>
      <div>
        <Router route={route} setRoute={setRoute}/>
      </div>
    </div>
  );
}

export default App;
