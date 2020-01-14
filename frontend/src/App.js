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
      <nav className="navbar navbar-expand-lg navbar-light">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <a className=" navbar-brand nav-link" href="#" onClick={() => setRoute(EVENTS_ROUTE)}>
              Events <span className="sr-only">(current)</span>
            </a>
            <a className="navbar-brand nav-link" href="#" onClick={() => setRoute(PLACES_ROUTE)}>Places</a>
          </div>
        </div>
      </nav>
      <div>
        <Router route={route} setRoute={setRoute}/>
      </div>
    </div>
  );
}

export default App;
