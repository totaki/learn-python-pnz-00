import React, { useState, useEffect } from 'react';
import { useHistory } from "react-router-dom";
import {AUTH_SUCCESS, EVENTS} from "./const";


const Auth = () => {
  const history = useHistory();
  let token_list = window.location.search.split('=');
  if (token_list[0] === '?token'){
    const token = token_list[1];
    localStorage.setItem('token', token);
    history.push(AUTH_SUCCESS);
  } else {
    history.push(EVENTS)
  }
  return null
};

const AuthSuccess = () => {
  const history = useHistory();
  alert('Login success!');
  history.push(EVENTS);
};


export default Auth
export {AuthSuccess}