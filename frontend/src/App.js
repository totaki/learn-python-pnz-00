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
} from "react-router-dom";
import './App.css';
import './bootstrap.min.css';
import Auth, {Auth_success, Logout} from "./Auth";
import Add_place from "./Addplace";


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
              <Link className={Check_authentication() ? "navbar-brand nav-link" : 'none'} to="/add_event">Добавить своё событие</Link>
              <Link className={Check_authentication() ? "navbar-brand nav-link" : 'none'} to="/add_place">Добавить место</Link>
          </div>
            <form className="form-inline">
              <button
                className={Check_authentication() ? "btn-outline-secondary btn-logout" : 'none'}
                type="submit"
                onClick={Logout()}>
                Logout
              </button>
            </form>
        </div>
      </nav>


      <Switch>
      {/*<Route path='/auth/success'>*/}
      {/*  <Auth_success />*/}
      {/*</Route>*/}
      {/*<Route path='/auth/logout'>*/}
      {/*  <Logout />*/}
      {/*</Route>*/}
        <Route path="/auth">
          <Auth />
        </Route>
        <Route path="/add_event">
          <AddEvent />
        </Route>
        <Route path="/add_place">
          <Add_place />
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

/**
 * @return {boolean}
 */
function Check_authentication() {
  const token = window.localStorage.getItem('token');
  let auth_flag = false;
  if (token){
    auth_flag = true
  }
  return auth_flag
}

export default App;
