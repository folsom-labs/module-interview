#!/usr/bin/env python2.7
# -*- coding:UTF-8 -*-

import unittest
import modules


class ModuleCase(unittest.TestCase):

    def test_1_module_operating_at_stc(self):
        '''
        Task 1: Create a (python) module with functions that describe a
        (solar) module. Load the module coefficients for the Trina TSM PA05
        from the CSV, set the temperature (T), to 25ºC and the irradiance (S)
        to 1000 W/m^2.

        This test will pass when you calculate voltage and current matching the
        correct numerical values along the (solar) module's I/V curve.
        '''

        (voltage, current) = modules.your_code_here()
        self.assertAlmostEquals(voltage, 5)
        self.assertAlmostEquals(current, 8.345847070106313,
                                msg='Current output at 5V is 8.34584 Amps')

        (voltage, current) = modules.your_code_here()
        self.assertAlmostEquals(voltage, 25)
        self.assertAlmostEquals(current, 8.276615347828452,
                                msg='Current output at 25V is 8.2766 Amps')

        (voltage, current) = modules.your_code_here()
        self.assertAlmostEquals(voltage, 34)
        self.assertAlmostEquals(current, 5.3462926879868,
                                msg='Current output at 34V is 5.3462 Amps')

    def test_2_module_operating_at_low_irradiance_high_temperature(self):
        '''
        Task 2:  Make sure your implementation produces accurate results at
        alternative irradiance and temperature levels.

        Here we used an irradiance of 600 W/m^2, and a temperature of 45ºC on
        the same Trina module as in Task 1.
        '''

        (voltage, current) = modules.your_code_here()
        self.assertAlmostEquals(voltage, 5)
        self.assertAlmostEquals(current, 5.001330819496669,
                                msg='Current output at 5V is 5.00133 Amps')

        (voltage, current) = modules.your_code_here()
        self.assertAlmostEquals(voltage, 15)
        self.assertAlmostEquals(current, 4.97041290811022,
                                msg='Current output at 15V is 4.9704 Amps')

        (voltage, current) = modules.your_code_here()
        self.assertAlmostEquals(voltage, 30)
        self.assertAlmostEquals(current, 4.048128130946268,
                                msg='Current output at 30V is 4.0481 Amps')

    def test_3_optimize_module_power(self):
        '''
        Task 3:  Usually, we don't just need to understand what the potential
        output of a solar module is (e.g. the I/V curve), we want to find out
        what voltage and current the module should be operating at in order to
        produce the most power.

        Write a function/method that determines the voltage and current along a
        modules I/V curve that maximizes power.  We won't tell you what the
        answer is, so also write the test that proves you found it.
        '''

        (voltage, current) = modules.your_code_here()
        assert False, "You didn't do anything yet"

    def test_4_optimize_module_power_extreme_conditions(self):
        '''
        Task 4: Write the tests to make sure your algorithm in Task 3 works
        for a range of module operating conditions and handles tricky edge
        cases correctly.

        For your reference, a module in the middle of the the Arizona desert
        at noon might have irradiance of ~1400 W/m^2.  A wintry London day
        might be 600 W/m^2.
        '''
        (voltage, current) = modules.your_code_here()
        assert False, "You didn't do anything yet"


if __name__ == "__main__":
    unittest.main()
