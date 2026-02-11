import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Teams component: Processed teams data:', teamsData);
        setTeams(teamsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams component: Error fetching data:', error);
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
            <p className="mt-3 text-white">Loading teams...</p>
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
          <h2 className="mb-0">👥 Teams</h2>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-hover align-middle">
              <thead>
                <tr>
                  <th>Team Name</th>
                  <th>Description</th>
                  <th>Members</th>
                  <th>Created Date</th>
                </tr>
              </thead>
              <tbody>
                {teams.length === 0 ? (
                  <tr>
                    <td colSpan="4" className="text-center py-4">
                      <em>No teams found</em>
                    </td>
                  </tr>
                ) : (
                  teams.map((team) => (
                    <tr key={team._id}>
                      <td><strong>{team.name}</strong></td>
                      <td>{team.description || <span className="text-muted">N/A</span>}</td>
                      <td>
                        <span className="badge bg-primary">{team.member_count || 0} members</span>
                      </td>
                      <td>{team.created_at ? new Date(team.created_at).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
          <div className="mt-3">
            <span className="badge bg-secondary">Total Teams: {teams.length}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Teams;
