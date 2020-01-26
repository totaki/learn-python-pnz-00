import React, { useState, useEffect } from 'react';
import Pagination from "./Pagination";
import {getItems} from "./api";
import {EVENTS} from "./const";


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
  const path = EVENTS;
  const [events, setEvents] = useState([]);
  const [url, setURL] = useState(null);
  const [pagination, setPagination] = useState([null, null]);

  const fetchCallback = (j) => {
      setEvents(j.results);
      setPagination([j.next, j.previous])
  };

  useEffect(() => {
    getItems({ url, path }, fetchCallback)
  }, [url, path]);

  const [next, previous] = pagination;

  return (
    <>
      <div>
        <h2 style={{textAlign: "center", marginBottom: 30, marginTop: 20}}>
          Список мероприятий
        </h2>
        <div>
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
