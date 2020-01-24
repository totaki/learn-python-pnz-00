import React, { useState, useEffect } from 'react';
import { useRouteMatch } from "react-router-dom";

const URL_ORIGIN = window.location.origin;
let path = '/events';

function Auth() {
  let token_list = window.location.search.split('=');
  // let path = '/auth/success';
  if (token_list[0] === '?token'){
    const token = token_list[1];
    localStorage.setItem('token', token);
    window.location.href = `${URL_ORIGIN}${path}`;
  }
  else
    path = '/events';
    // window.location.href = `${URL_ORIGIN}${path}`;
}

function Auth_success() {
    alert('Login success!');
    let path = '/events';
    window.location.href = `${URL_ORIGIN}${path}`;
}

function Logout() {
  window.localStorage.removeItem('token')
  // window.location.href = `${URL_ORIGIN}${path}`;
}

export default Auth
export {Auth_success, Logout}