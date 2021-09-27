import React from 'react'
import {Link, useHistory } from "react-router-dom";

const NavBar = () => {

  const history = useHistory()
  const logout = () => {
      window.localStorage.removeItem('token')
      history.push('/events')
  };

  /**
 * @return {boolean}
 */
  function checkAuthentication() {
    const token = window.localStorage.getItem('token');
    let auth_flag = false;
    if (token){
      auth_flag = true
    }
    return auth_flag
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-light">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <Link className="navbar-brand nav-link" to="/">События</Link>
            <Link className="navbar-brand nav-link" to="/places">Места</Link>
            <Link className={checkAuthentication() ? "navbar-brand nav-link" : 'none'} to="/events/add">Добавить своё событие</Link>
            <Link className={checkAuthentication() ? "navbar-brand nav-link" : 'none'} to="/places/add">Добавить место</Link>
          </div>
            <button
              className={checkAuthentication() ? "btn-outline-secondary btn-logout" : 'none'}
              type="submit"
              onClick={logout}>
              Logout
            </button>
        </div>
      </nav>

  )
};

export default NavBar