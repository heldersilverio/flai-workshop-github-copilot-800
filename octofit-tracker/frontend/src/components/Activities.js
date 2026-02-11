import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Activities component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Activities component: Processed activities data:', activitiesData);
        setActivities(activitiesData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities component: Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="d-flex justify-content-center align-items-center" style={{minHeight: '400px'}}>
          <div className="text-center">
            <div className="spinner-border text-primary" role="status">
              <span className="visually-hidden">Loading...</span>
            </div>
            <p className="mt-3 text-white">Loading activities...</p>
          </div>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header">
          <h2 className="mb-0">🏃 Activities</h2>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-hover align-middle">
              <thead>
                <tr>
                  <th>User</th>
                  <th>Type</th>
                  <th>Duration (min)</th>
                  <th>Distance (km)</th>
                  <th>Calories</th>
                  <th>Date</th>
                </tr>
              </thead>
              <tbody>
                {activities.length === 0 ? (
                  <tr>
                    <td colSpan="6" className="text-center py-4">
                      <em>No activities found</em>
                    </td>
                  </tr>
                ) : (
                  activities.map((activity) => (
                    <tr key={activity._id}>
                      <td><strong>{activity.user_id}</strong></td>
                      <td>
                        <span className="badge bg-info">{activity.activity_type}</span>
                      </td>
                      <td>{activity.duration}</td>
                      <td>{activity.distance || <span className="text-muted">N/A</span>}</td>
                      <td>
                        <span className="badge bg-warning text-dark">{activity.calories} cal</span>
                      </td>
                      <td>{activity.date ? new Date(activity.date).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
          <div className="mt-3">
            <span className="badge bg-secondary">Total Activities: {activities.length}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Activities;
