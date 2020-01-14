import React, { useState, useEffect } from 'react';
import { BASE_API_URL } from "./const";
import Pagination from "./Pagination";

const EVENTS_ROUTE = 'events';


function Event({ title, body, event_date }) {
  return (

        <div className="col-md-4">
          <div className="card mb-4 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">{title}</h5>
              <p className="card-text">{body}</p>
              <p>{event_date}</p>
            </div>
          </div>
        </div>

  )
}


function Events({ setRoute }) {
  const [events, setEvents] = useState([]);
  const [url, setURL] = useState(`${BASE_API_URL}/events/`);
  const [pagination, setPagination] = useState([null, null]);

  useEffect(() => {
    fetch(url)
      .then(result => result.json())
      .then(json => {
        setEvents(json.results);
        setPagination([json.next, json.previous])
      })
      .catch(e => console.log(e));
  }, [url]);

  const [next, previous] = pagination;

  return (
    <>
      <div className="container">
        <h1 style={{textAlign: "center"}}>Список мероприятий</h1>
          <div className="container">
            <div className="row">
              {events.map((e, i) => <Event {...e}/>)}
              </div>
          </div>
        <Pagination
          next={next}
          previous={previous}
          setURL={setURL}
        />
      </div>
    </>
  )
}

export default Events
export {
  EVENTS_ROUTE
}
