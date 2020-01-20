import React, { useState } from 'react';
import Events, { EVENTS_ROUTE } from "./Events";
import Places, { PLACES_ROUTE } from "./Places";
import Add_event, { ADD_EVENT_ROUTE } from "./Addevent";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';
import './bootstrap.min.css';


function App() {
  console.log(window.location.path)
  return (
    <Router>
    <div className="container">
      <nav className="navbar navbar-expand-lg navbar-light">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
              <Link className="navbar-brand nav-link" to="/">События</Link>
              <Link className="navbar-brand nav-link" to="/places">Места</Link>
              <Link className="navbar-brand nav-link" to="/add_event">Добавить своё событие</Link>
          </div>
        </div>
      </nav>


      <Switch>
        <Route path="/add_event">
          <Add_event />
        </Route>
        <Route path="/places">
          <Places />
        </Route>
        <Route path="/">
          <Events />
        </Route>
      </Switch>
    </div>
    </Router>
  );
}

export default App;
