from ...app import app
import json
import os


class TestOperations():
  def test_sum_two_number(self):
    with app.test_client() as test_client:
      response = test_client.post(
        '/sum', json={
          'x': 5,
          'y': 6
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 200
      assert 'sum' in response_json
      assert 'version' in response_json