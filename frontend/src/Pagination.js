import React, {useEffect, useState}  from "react";


function Pagination(props){

  return (
    <>
      <div className="btn-group" role="group" aria-label="paginationGroup">
        {props.previous ? <button  type="button" className="btn btn-secondary" onClick={() => props.setURL(props.previous)}>Previous</button> : null}
        {props.next ? <button  type="button" className="btn btn-secondary" onClick={() => props.setURL(props.next)}>Next</button> : null}
      </div>
    </>
  )
}

export default Pagination
