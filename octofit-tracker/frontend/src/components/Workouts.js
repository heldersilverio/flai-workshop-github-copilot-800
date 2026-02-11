import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Workouts component: Processed workouts data:', workoutsData);
        setWorkouts(workoutsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts component: Error fetching data:', error);
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
            <p className="mt-3 text-white">Loading workouts...</p>
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
          <h2 className="mb-0">💪 Workout Suggestions</h2>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-hover align-middle">
              <thead>
                <tr>
                  <th>Workout Name</th>
                  <th>Type</th>
                  <th>Duration (min)</th>
                  <th>Difficulty</th>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody>
                {workouts.length === 0 ? (
                  <tr>
                    <td colSpan="5" className="text-center py-4">
                      <em>No workouts found</em>
                    </td>
                  </tr>
                ) : (
                  workouts.map((workout) => (
                    <tr key={workout.id}>
                      <td><strong>{workout.name}</strong></td>
                      <td>
                        <span className="badge bg-info">{workout.workout_type || workout.type}</span>
                      </td>
                      <td>
                        <span className="badge bg-secondary">{workout.duration_minutes} min</span>
                      </td>
                      <td>
                        <span className={`badge bg-${
                          workout.difficulty === 'Easy' ? 'success' : 
                          workout.difficulty === 'Medium' ? 'warning text-dark' : 
                          'danger'
                        }`}>
                          {workout.difficulty}
                        </span>
                      </td>
                      <td>{workout.description || <span className="text-muted">N/A</span>}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
          <div className="mt-3">
            <span className="badge bg-secondary">Total Workouts: {workouts.length}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
