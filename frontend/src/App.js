import React, { useState } from 'react';
import Events, { EVENTS_ROUTE } from "./Events";
import Places, { PLACES_ROUTE } from "./Places";
import AddEvent, { ADD_EVENT_ROUTE } from "./Addevent";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
  useHistory,
} from "react-router-dom";
import './App.css';
import './bootstrap.min.css';
import Auth, {AuthSuccess} from "./Auth";
import AddPlace from "./Addplace";
import NavBar from "./NavBar";


function App() {

  console.log(window.location.path);

  return (
    <Router>
    <div className="container">
      <NavBar />

      <Switch>
        <Route path="/auth">
          <Auth />
        </Route>
        <Route path="/auth/success">
          <AuthSuccess />
        </Route>
        <Route path="/events/add">
          <AddEvent />
        </Route>
        <Route path="/places/add">
          <AddPlace />
        </Route>
        <Route path="/places">
          <Places />
        </Route>
        <Route path="/events">
          <Events />
        </Route>
        <Redirect from='/' to='/events'/>
      </Switch>
    </div>
    </Router>
  );
}



export default App;
